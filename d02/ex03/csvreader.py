import os.path


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.skip_top = skip_top
        if header:
            self.skip_top += 1
        self.skip_bottom = skip_bottom
        self.header = header
        self.header_line = None
        self.getdata_done = False
        self.corrupt = False

    def __enter__(self):
        if not os.path.isfile(self.filename):
            self.corrupt = True
            return None
        self.file = open(self.filename, 'r')
        return self

    def __exit__(self, type, value, traceback):
        if not self.corrupt:
            self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list (list(list, list, ...)) representing the data.
        """
        if self.corrupt:
            return None
        if self.getdata_done == True:
            return self.reader
        lines = self.file.readlines()
        reader = []
        nb_elt = len(lines[0].split(self.sep))
        len_lines = len(lines)
        for i in range(len_lines):
            if not self.header or i != 0:
                if self.skip_top > i or i > len_lines - self.skip_bottom - 1:
                    continue
            tabLines = lines[i][:len(lines[i]) - 1].split(self.sep)
            if len(tabLines) != nb_elt or tabLines.count('') != 0:
                self.corrupt = True
                return None
            tmp = []
            for elt in tabLines:
                if elt == '':
                    self.corrupt = True
                    return None
                if len(elt.split('"')) == 3:
                    tmp.append(elt.split('"')[1])
                elif len(elt.split('[')) != 1:
                    tmp.append(elt.lstrip().rstrip())
                else:
                    tmp.append(int(elt.lstrip().rstrip()))
            if self.header and i == 0:
                self.header_line = tmp
            else:
                reader.append(tmp)
        self.reader = reader
        self.getdata_done = True
        if self.corrupt:
            return None
        return reader

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if not self.header:
            return None
        if self.header_line is None:
            self.getdata()
        if self.corrupt:
            return None
        return self.header_line
