def int_to_key(num):
    if num == 0:
        return ""

    return "{0}{1}".format(
        int_to_key(num // 2),
        '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[num % 52]
    )


import shortuuid

print(shortuuid.uuid(name="5", length=16))
