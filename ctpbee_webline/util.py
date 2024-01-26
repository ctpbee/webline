from hashlib import md5


def encrypt(string: str) -> str:
    md = md5(string=string.encode("utf8"))
    return md.hexdigest()
