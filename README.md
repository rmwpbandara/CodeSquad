# Sketch-to-Html
Final Year Group Project - Group Coder's Cafe<br>Batch 14, Faculty of Information Technology, University of Moratuwa, Sri Lanaka.

<h2>Guide Line For Configarations </h2>

install git to mechine => <a> "https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-64-bit.exe" </a><br>
install python 3.6.6 => <a> "https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe"</a><br>
install tesseract ocr engine =><a> "https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.0.0.20181030.exe"</a><br>
install node => <a> "https://nodejs.org/dist/v10.15.3/node-v10.15.3-x64.msi"</a><br>

<h3> use <code> git clone https://github.com/rmwpbandara/Sketch-to-Html.git </code> to clone project</h3>
<h3>open command prompt in machine, and run these command in command prompt.</h3>
	<code> py -m pip install --upgrade pip</code><br>
	<code> py -m pip install --user virtualenv</code><br>
	<code> npm install http-server</code><br>
	<code> npm install http-server -g</code><br>
<h3>open command prompt in projet folder, and run these command in command prompt.</h3>
	<code> py -m virtualenv venv</code><br>
	<code> .\venv\Scripts\activate</code><br>
	<code> where python </code>----> Output Shows like "path"/env/bin/python.exe<br>
	<code> pip install opencv-python==3.4.5.20</code><br>
	<code> pip install pytesseract==0.2.6</code><br>
	<code> pip install flask==1.0.2</code><br>
<h3>doubleclick app.py </h3>
<h3>You Can Upload Your images from only <code> "project folder root/input/"</code>  path.</h3>

<h3>Libraries</h3>
<ul> 
	<li>Python 3.6.6</li>
	<li>OpenCV python 3.4.5.20</li>
	<li>Pytesseract 0.2.6</li>
	<li>Numpy 1.16.1</li>
	<li>Pillow 5.4.1</li>
	<li>Pip 19.0.3</li>
	<li>Flask 1.0.2</li>
</ul>
<h3>Drawing shape and writing text</h3>
<ul>
	<li>When drawing shape cannot be intersect and all corners must be joining each other’s.</li>
	<li>Cannot be draw shape haven't any gap between the other shape.</li>
	<li>Writing text are cannot be connect any line of the shape.</li>
	<li>When writing a text write a clearly and do not write unclearly or cursive letter.</li>
	<li>When writing text using high thickness red color pen. </li>
	<li>There should be a label for each and every input field, radio button and option button.</li> 
	<li>Every radio button group check box group and drop downs should have a main label.</li>
	<li>The images that drawn for web pages in a site, should save with its display name of the hyperlink.</li>
</ul>
<h3>Process</h3>
<ul>
	<li>Double click app.py file</li>
	<li>Type the Number of uploaded page amount and click anywhere of the web page after can be browse and upload images.</li>
	<li>Only can be upload images should be in " project_folder/input/ " folder.</li>
	<li>Cannot be change selected images. If need to change, please refresh the page and upload the image using before process.</li>
	<li>When saving the image must using relevant page content name as the image name.</li>
	<li>Click the generate button.</li>
	<li>Wait some time to the process, you can download zip file from browser and unzip the folder and show the html page.</li>
</ul>
<ul>
<h3>Segmentation Module</h3>
	<li><code>pip install -r requirements.txt</code></li>
	<li><code>pip install onnx</code></li>
	<li><code>python export.py --weights runs/train/exp2/weights/last.pt --include torchscript onnx</code></li>
	<li><code>pip install opencv-contrib-python</code></li>
	<li>run segementation.py file</li>
	
	
	 YOLOV5 <a>https://drive.google.com/drive/folders/1UnoNeNqVi6w5rD4IDqXDmvzGqk7NO5MZ?usp=sharing</a> 
</ul>
