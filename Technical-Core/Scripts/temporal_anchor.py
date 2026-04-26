import os
import tarfile

def secure_black_box():
    print("[!] LEVEL 19 TEMPORAL ANCHOR: Creating hidden logic echo...")
    source_dir = os.path.expanduser("~/Sentinel-Core/Vault")
    # Hiding the backup in a non-obvious system path
    output_filename = os.path.expanduser("~/.sentinel_echo.tgz")
    
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    print(f"[+] Black Box anchored: {output_filename}")

if __name__ == "__main__":
    secure_black_box()
