

class Marker:
    def __init__(self, length):
        self.__length = length

    def __len__(self):
        return self.__length

    def is_valid(self, buf):
        return len(buf) == self.__length and len(buf) == len(set(buf))

    def find_next(self, buf):
        buflen = len(buf)
        pos = 0

        while pos + self.__length <= buflen:
            candidate = buf[pos:pos + self.__length]
            if self.is_valid(candidate):
                pos += self.__length
                yield pos
            else:
                pos += 1

class PackageMarker(Marker):
    def __init__(self):
        super().__init__(4)

class MessageMarker(Marker):
    def __init__(self):
        super().__init__(14)

buffer = ""
with open('input_6dec.txt', 'r') as f:
    buffer = f.readline()

package_loc = PackageMarker().find_next(buffer)
message_loc = MessageMarker().find_next(buffer)

print("Part 1: %d" % next(package_loc))
print("Part 2: %d" % next(message_loc))
