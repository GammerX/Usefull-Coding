def zipstring(string):
    if type(string) is not str:
        raise TypeError("expected string, " + str(type(string)) + " found")

    compressed_string = []
    precedent_letter = (-1, "Impossible")

    for letter in enumerate(list(string)):
        if precedent_letter[1] != letter[1]:
            if len(compressed_string) > 1 and compressed_string[-1][1] == 1:
                del compressed_string[-1][1]
            compressed_string.append([letter[1], 1])
            precedent_letter = letter
        else:
            compressed_string[-1][1] += 1
    return compressed_string


def unzipstring(zipped_string):
    if type(zipped_string) is not list:
        raise TypeError("expected list, " + str(type(zipped_string)) + " found")
    decompressed_string = ""

    for compressed_data in zipped_string:
        if len(compressed_data) == 1:
            decompressed_string += compressed_data[0]
        else:
            decompressed_string += compressed_data[0] * compressed_data[1]
