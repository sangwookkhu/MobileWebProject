import os
import socket
import re
from datetime import datetime

class SocketServer:
    def __init__(self):
        self.bufsize = 4096  # 버퍼 크기 증가 (이미지 처리를 위해)
        with open('./response.bin', 'rb') as file:
            self.RESPONSE = file.read()  # 응답 파일 읽기
        self.DIR_PATH = './request'
        self.IMAGE_PATH = './images'
        self.createDir(self.DIR_PATH)
        self.createDir(self.IMAGE_PATH)

    def createDir(self, path):
        """디렉토리 생성"""
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except OSError:
            print(f"Error: Failed to create the directory {path}.")

    def parse_multipart_data(self, data, boundary):
        """멀티파트 데이터에서 이미지 파일 추출"""
        try:
            # boundary로 데이터 분리
            parts = data.split(boundary.encode())
            
            for part in parts:
                if b'Content-Type: image/' in part:
                    # Content-Disposition에서 파일명 추출
                    headers_end = part.find(b'\r\n\r\n')
                    if headers_end == -1:
                        continue
                    
                    headers = part[:headers_end].decode('utf-8', errors='ignore')
                    file_data = part[headers_end + 4:]
                    
                    # 파일명 추출
                    filename_match = re.search(r'filename="([^"]+)"', headers)
                    if filename_match:
                        original_filename = filename_match.group(1)
                    else:
                        # 확장자 추출
                        content_type_match = re.search(r'Content-Type: image/(\w+)', headers)
                        ext = content_type_match.group(1) if content_type_match else 'jpg'
                        original_filename = f'uploaded_image.{ext}'
                    
                    # 타임스탬프와 함께 파일명 생성
                    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                    name, ext = os.path.splitext(original_filename)
                    new_filename = f"{timestamp}_{name}{ext}"
                    
                    # 마지막 boundary 제거
                    if file_data.endswith(b'--\r\n'):
                        file_data = file_data[:-4]
                    elif file_data.endswith(b'\r\n'):
                        file_data = file_data[:-2]
                    
                    # 이미지 파일 저장
                    image_path = os.path.join(self.IMAGE_PATH, new_filename)
                    with open(image_path, 'wb') as f:
                        f.write(file_data)
                    
                    print(f"Image saved: {new_filename}")
                    return True
            
            return False
            
        except Exception as e:
            print(f"Error parsing multipart data: {e}")
            return False

    def run(self, ip, port):
        """서버 실행"""
        # 소켓 생성
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((ip, port))
        self.sock.listen(10)
        print("Start the socket server...")
        print("\"Ctrl+C\" for stopping the server!\r\n")
        
        try:
            while True:
                # 클라이언트의 요청 대기
                clnt_sock, req_addr = self.sock.accept()
                clnt_sock.settimeout(10.0)  # 타임아웃 설정 (10초)
                print(f"Connection from {req_addr[0]}:{req_addr[1]}")
                
                try:
                    # 전체 요청 데이터 수신
                    request_data = b""
                    while True:
                        try:
                            chunk = clnt_sock.recv(self.bufsize)
                            if not chunk:
                                break
                            request_data += chunk
                            
                            # HTTP 요청의 끝을 확인
                            if b'\r\n\r\n' in request_data:
                                # Content-Length 확인
                                headers = request_data.split(b'\r\n\r\n')[0].decode('utf-8', errors='ignore')
                                content_length_match = re.search(r'Content-Length: (\d+)', headers)
                                
                                if content_length_match:
                                    content_length = int(content_length_match.group(1))
                                    header_end = request_data.find(b'\r\n\r\n') + 4
                                    
                                    # 전체 데이터를 받을 때까지 계속 수신
                                    while len(request_data) - header_end < content_length:
                                        chunk = clnt_sock.recv(self.bufsize)
                                        if not chunk:
                                            break
                                        request_data += chunk
                                    break
                                else:
                                    break
                                    
                        except socket.timeout:
                            break
                    
                    if request_data:
                        # 실습 1: 원본 요청을 bin 파일로 저장
                        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                        bin_filename = f"{timestamp}.bin"
                        bin_filepath = os.path.join(self.DIR_PATH, bin_filename)
                        
                        with open(bin_filepath, 'wb') as f:
                            f.write(request_data)
                        
                        print(f"Request saved to: {bin_filename}")
                        print(f"Client IP: {req_addr[0]}, Port: {req_addr[1]}")
                        
                        # 실습 2: 멀티파트 데이터에서 이미지 추출
                        request_str = request_data.decode('utf-8', errors='ignore')
                        if 'multipart/form-data' in request_str:
                            boundary_match = re.search(r'boundary=([^\r\n;]+)', request_str)
                            if boundary_match:
                                boundary = '--' + boundary_match.group(1).strip()
                                self.parse_multipart_data(request_data, boundary)
                    
                except socket.timeout:
                    print("Socket timeout occurred")
                except Exception as e:
                    print(f"Error processing request: {e}")
                
                # 응답 전송
                try:
                    clnt_sock.sendall(self.RESPONSE)
                except:
                    pass
                
                # 클라이언트 소켓 닫기
                clnt_sock.close()
                print("Connection closed\n")
                
        except KeyboardInterrupt:
            print("\r\nStop the server...")
        finally:
            # 서버 소켓 닫기
            self.sock.close()

if __name__ == "__main__":
    server = SocketServer()
    server.run("127.0.0.1", 8000)