#Dictionary -  Marker : ((255, byte), Marker Name; Description, 1/0 Common/Uncommon, 1/0 has length header)
markerDict = {
    'SOF0' : ((255, 192), 'Start of Frame 0; Baseline DCT', 1, 1),
    'SOF1' : ((255, 193), 'Start of Frame 1; Extended Sequential DCT', 1, 1),
    'SOF2' : ((255, 194), 'Start of Frame 2; Progressive DCT', 1, 1),
    'SOF3' : ((255, 195), 'Start of Frame 3; Lossless (sequential)', 1, 1),
    'DHT' : ((255, 196), '  Define Huffman Table', 1, 1),
    'SOF5' : ((255, 197), 'Start of Frame 5; Differential sequential DCT', 1, 1),
    'SOF6' : ((255, 198), 'Start of Frame 6; Differential progressive DCT', 1, 1),
    'SOF7' : ((255, 199), 'Start of Frame 7; Differential lossless (sequential)', 1, 1),
    'JPG' : ((255, 200), 'JPEG Extensions', 1, 0),
    'SOF9' : ((255, 201), 'Start of Frame 9; Extended sequential DCT, Arithmetic coding', 1, 1),
    'SOF10' : ((255, 202), 'Start of Frame 10; Progressive DCT, Arithmetic coding', 1, 1),
    'SOF11' : ((255, 203), 'Start of Frame 11; Lossless (sequential), Arithmetic coding', 1, 1),
    'DAC' : ((255, 204), 'Define Arithemtic Coding', 1, 0),
    'SOF13' : ((255, 205), 'Start of Frame 13;Differential DCT, Arithmetic coding', 1, 1),
    'SOF14' : ((255, 206), 'Start of Frame 14; Differential progressive DCT, Arithmetic coding', 1, 1),
    'SOF15' : ((255, 207), 'Start of Frame 15; Differential lossless (sequential), Arithmetic coding', 1, 1),
    'RST0' : ((255, 208), 'Reset Marker 0', 1, 0),
    'RST1' : ((255, 209), 'Reset Marker 1', 1, 0),
    'RST2' : ((255, 210), 'Reset Marker 2', 1, 0),
    'RST3' : ((255, 211), 'Reset Marker 3', 1, 0),
    'RST4' : ((255, 212), 'Reset Marker 4', 1, 0),
    'RST5' : ((255, 213), 'Reset Marker 5', 1, 0),
    'RST6' : ((255, 214), 'Reset Marker 6', 1, 0),
    'RST7' : ((255, 215), 'Reset Marker 7', 1, 0),
    'SOI' : ((255, 216), 'Start of Image', 1, 0),
    'EOI' : ((255, 217), 'End of Image', 1, 0),
    'SOS' : ((255, 218), 'Start of Scan', 1, 1),
    'DQT' : ((255, 219), 'Define Quantization Table', 1, 1),
    'DNL' : ((255, 220), 'Define Number of Lines', 0, 0),
    'DRI' : ((255, 221), 'Define Restart Interval', 1, 0),
    'DHP' : ((255, 222), 'Define Hierarchical Progression', 0, 0),
    'EXP' : ((255, 223), 'Expand Reference Component', 0, 0),
    'APP0' : ((255, 224), 'Application Segment 0 - JFIF JPEG Image/Motion JPEG(MJPG)', 1, 1),
    'APP1' : ((255, 225), 'Application Segment 1 - EXIF Metadata, TIFF IFD format/JPEG Thumbnail(160x120)/Adobe XMP', 1, 1),
    'APP2' : ((255, 226), 'Application Segment 2; ICC color profile/FlashPix', 1, 1),
    'APP3' : ((255, 227), 'Application Segment 3; JPS Tag for Steroscopic JPEG images', 0, 1),
    'APP4' : ((255, 228), 'Application Segment 4', 0, 1),
    'APP5' : ((255, 229), 'Application Segment 5', 0, 1),
    'APP6' : ((255, 230), 'Application Segment 6; NITF Lossles profile', 0, 1),
    'APP7' : ((255, 231), 'Application Segment 7', 0, 1),
    'APP8' : ((255, 232), 'Application Segment 8', 0, 1),
    'APP9' : ((255, 233), 'Application Segment 9', 0, 1),
    'APP10' : ((255, 234), 'Application Segment 10; ActiveObject (multimedia messages + captions)', 0, 1),
    'APP11' : ((255, 235), 'Application Segment 11; HELIOS JPEG Resources (OPI Postscript)', 0, 1),
    'APP12' : ((255, 236), 'Application Segment 12; Picture Info (older digicams)/Photoshop Save for Web:Ducky', 1, 1),
    'APP13' : ((255, 237), 'Application Segment 13; Photoshop Save As: IRB, 8BIM, IPTC', 1, 1),
    'APP14' : ((255, 238), 'Application Segment 14', 0, 1),
    'APP15' : ((255, 239), 'Application Segment 15', 0, 1),
    'JPG0' : ((255, 240), 'JPEG Extenstion 0', 0, 0),
    'JPG1' : ((255, 241), 'JPEG Extenstion 1', 0, 0),
    'JPG2' : ((255, 242), 'JPEG Extenstion 2', 0, 0),
    'JPG3' : ((255, 243), 'JPEG Extenstion 3', 0, 0),
    'JPG4' : ((255, 244), 'JPEG Extenstion 4', 0, 0),
    'JPG5' : ((255, 245), 'JPEG Extenstion 5', 0, 0),
    'JPG6' : ((255, 246), 'JPEG Extenstion 6', 0, 0),
    'JPG7' : ((255, 247), 'JPEG Extenstion 7', 1, 0),
    'JPG8' : ((255, 248), 'JPEG Extenstion 8; Lossless JPEG Extension Parameters', 1, 0),
    'JPG9' : ((255, 249), 'JPEG Extenstion 9', 0, 0),
    'JPG10' : ((255, 250), 'JPEG Extenstion 10', 0, 0),
    'JPG11' : ((255, 251), 'JPEG Extenstion 11', 0, 0),
    'JPG12' : ((255, 252), 'JPEG Extenstion 12', 0, 0),
    'JPG13' : ((255, 253), 'JPEG Extenstion 13', 0, 0),
    'COM' : ((255, 254), 'Comment', 1, 1),
    }