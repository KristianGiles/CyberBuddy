import vt
import pprint

def create_client():
    client = vt.Client("414b50b7880a450854ead661dff30427b5230d147be6e7193c4cb7857ff44615")

    return client

def kill_client(client):
    client.close()

### File Details
def file_information(file):
    client = create_client()

    file = client.get_object(file)
    try:
        print(f"File Size: {file.size}")
        print(f"SHA256 Hash: {file.sha256}")
        print(f"FIle Type: {file.type_tag}")
        pprint.pprint(file.last_analysis_state)
    except Exception as e:
        print(e)

        kill_client(client)