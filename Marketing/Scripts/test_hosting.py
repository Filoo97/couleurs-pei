
import requests
import os

def test_upload():
    # Create a dummy image first
    dummy_path = "test_upload.txt"
    with open(dummy_path, "w") as f:
        f.write("test content")

    url = "https://tmpfiles.org/api/v1/upload"
    files = {'file': open(dummy_path, 'rb')}
    
    print("Uploading to tmpfiles.org...")
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        data = response.json()
        print("Success!")
        print(data)
        # Construct direct URL
        # Usually tmpfiles returns a url like https://tmpfiles.org/12345/file.txt
        # The direct download url is https://tmpfiles.org/dl/12345/file.txt
        url_obj = data['data']['url']
        direct_url = url_obj.replace('tmpfiles.org/', 'tmpfiles.org/dl/')
        print(f"Direct URL: {direct_url}")
    else:
        print(f"Failed: {response.status_code}")
        print(response.text)

    os.remove(dummy_path)

if __name__ == "__main__":
    test_upload()
