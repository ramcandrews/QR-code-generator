import qrcode
import re


# This requires openCV and it's QR-code module to be installed. and maybe pillow depending on your system
# pip3 install opencv-python qrcode Pillow

def make_QR(label, data, width=256, filetype="PNG"):
    size = [(width, width),
            (int(width/2), int(width/2)),
            (width*2, width*2)]

    # generate qr code(s)
    if label is False:
        # output file name
        label = re.sub('https?://+', '', data)
        label = label.replace("/", "")
        label = label.replace(" ", "_")
        label = label.replace(".", "_")
        label = label.lower()
        
        for choice in size:
            img = qrcode.make(data).resize(choice)
            # output file name
            filename = label + '_' + str(choice[0]) + "." + filetype
            # save img to a file
            img.save(filename, format=filetype, include_color_table=False, optimize=True, comment="Robotrodeo.net (c) 2020")

    else:
        # output file name
        img = qrcode.make(data).resize((width, width))
        label = label.replace("/", "")
        label = label.replace(" ", "_")
        label = label.lower()
        filename = label + "." + filetype
        # save img to a file
        img.save(filename, format=filetype, include_color_table=False, optimize=True, comment="Robotrodeo.net (c) 2020")

make_QR("Label -optional! It can read from the data variable", "Data such as a URL")
