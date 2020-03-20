# QR-code-generator
I can't figure out if QR code apps are trustworthy or not so I am making my own (this one is trustworthy). 

I use QR codes to pass strings to my phone from my desktop, I also want to start using QR codes for all kinds of things. This will help me make QR codes in an automated fashion and in a really quick one-off fashion.

## Parameters:
**label:** Describe the puporse of the code, and set the file name. If a URL is used in the data field then type False.

**data:** This is the data that will be encoded into a QR image.

**width:** (default = 256) This is the width of a square image. The output will be halved and doubled for URLs for a total of 3 output images.

**filetype:** (default = "PNG") For somereason PNG outputs the smalles file size by a factor of 10. all images up to 512w end up being less than 1kb. I will be interested in learning how to output a vector image (SVG).

## Usage
`make_QR("Funny joke", "This is a funny jonk")`

## Output
filename: 
`funny_joke.PNG`
![Image - QR code example](https://github.com/ramcandrews/QR-code-generator/blob/master/funny_joke.PNG)


## Roadmap --> 0.???
I created this script to solve a specific problem, but I also think it would be kind of cool to develop into a more useful and general tool. This project will either continue to be develped into a CLI app and eventually a Tkinter or flask app or will die on the vine.

### Next Features
1. Build out the regex to replace the chain of .replace() functions and to minimize duplicate code.
2. Insert the label to the image border. I would have already done it but I have to figure out the exact pixel coordinates of where I want the label to be placed.
