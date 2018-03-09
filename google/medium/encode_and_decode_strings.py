# 271 Encode and Decode Strings
# 
# Design an algorithm to encode a list of strings to a string. 
# 
# The encoded string is then sent over the network and is decoded back to the original list of strings.
# 
# Machine 1 (sender) has the function:
# 
# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }

class Codec(object):
    def encode(self, strs):
        encodeStr = ''
        for s in strs:
            encodeStr += str(len(s))+'#'+s
        return encodeStr

    def decode(self, s):
        res, i = [], 0
        while i < len(s):
            if s[i] == '#':
                start = i + 1
                end = int(s[i-1]) + i
                res.append(s[start:end+1])
                i = end + 1
            else:
                i += 1
        return res

if __name__ == '__main__':
    codec = Codec()
    strs = ['1234', 'abcd4', '4345', '###', '', '   ']
    s = codec.encode(strs)
    assert codec.decode(s) == strs 