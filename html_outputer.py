class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('new-output.html', 'w', encoding='utf-8')

        fout.write("<html>")
        fout.write("<meta charset='utf-8'>")
        fout.write("<body>")
        fout.write("<table>")
        print(self.datas)
        for data in self.datas:

            for x in range(100):
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['item%s' % (x)]['name'])
                fout.write("<td>%s</td>" % data['item%s' % (x)]['price'])
                fout.write("<td>%s</td>" % data['item%s' % (x)]['game'])
                fout.write("<td>%s</td>" % data['item%s' % (x)]['quantity'])
                fout.write("</tr>")
            print("Write success!")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
