import base64

def decode_string(encoded_string, encoding="base64"):
    try:
        if encoding.lower() == "base64":
            decoded_bytes = base64.b64decode(encoded_string)
        else:
            raise ValueError("Unsupported encoding")

        decoded_string = decoded_bytes.decode("utf-8")
        return decoded_string
    except Exception as e:
        return f"Error decoding string: {str(e)}"

if __name__ == "__main__":
    # Input the encoded string and encoding type
    encoded_string = input("Enter the encoded string: ")
    encoding_type = input("Enter the encoding type (default is base64): ") or "base64"

    # Call the function and print the result
    decoded_result = decode_string(encoded_string, encoding_type)
    print(f"Decoded string: {decoded_result}")
