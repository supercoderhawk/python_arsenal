_LINE_BREAKS = '\n\v\x0b\f\x0c\x1c\x1d\x1e\x85\u2028\u2029'

def read_lines(filename, encoding=_ENCODING_UTF8, strip=False, skip_empty=False):
    :param strip: whether strip every line, default is False
    :param skip_empty: whether skip empty line, when strip is False, judge after strip
            if skip_empty:
            if skip_empty:
                lines = []
                for line in f.read().splitlines(True):
                    line = line.strip(_LINE_BREAKS)
                    if line:
                        lines.append(line)
                return lines
                return [l.strip(_LINE_BREAKS) for l in f.read().splitlines(True)]
        self._file = None
    def close(self):
        if self._file is not None and not self._file.closed:
            self._file.close()

    def __change_mode(self, mode):
        if not self._file:
            self._file = open(self.filename, mode, encoding=self.encoding)
        elif mode == 'r' or self._file.mode != mode:
            self._file.close()
            self._file = open(self.filename, mode, encoding=self.encoding)
        self.close()
        return self._file.read()
        for line in self._file:
        self._file.write(data)
        self._file.writelines(new_lines)
        self._file.write(data)
            self._file.write(line)
        for line in self._file:
        self._file.write(self._to_string(item))
        self._file.append(self._to_string(line))