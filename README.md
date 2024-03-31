
<h1>Image Viewer App</h1>

<p>This is a simple image viewer application implemented using Python's Tkinter library. It allows users to navigate through a series of images.</p>

<h2>Instructions</h2>

<ol>
    <li><strong>Installation:</strong></li>
    <ul>
        <li>Ensure you have Python installed on your system.</li>
        <li>Install necessary libraries using pip:</li>
        <code>pip install pillow</code>
    </ul>
    <li><strong>Execution:</strong></li>
    <ul>
        <li>Run the Python script <code>image_viewer.py</code>.</li>
        <li>The application window will open displaying the first image in the series.</li>
        <li>You can navigate through the images using the navigation buttons (<code>&lt;&lt;</code> and <code>&gt;&gt;</code>).</li>
        <li>To exit the application, click the EXIT button.</li>
    </ul>
</ol>

<h2>Dependencies</h2>
<ul>
    <li>Python 3.x</li>
    <li>Pillow (Python Imaging Library)</li>
</ul>

<h2>Usage</h2>

<p><strong>Navigation Buttons:</strong></p>
<ul>
    <li><code>&lt;&lt;</code>: Click this button to move to the previous image.</li>
    <li><code>&gt;&gt;</code>: Click this button to move to the next image.</li>
    <li><em>Note:</em> Navigation buttons are disabled at the first and last images respectively.</li>
</ul>

<p><strong>Exit Button:</strong></p>
<ul>
    <li>Click the EXIT button to close the application.</li>
</ul>

<h2>File Structure</h2>
<ul>
    <li><code>image_viewer.py</code>: Python script for the image viewer application.</li>
    <li><code>Images/</code>: Directory containing the images to be displayed by the application.</li>
</ul>

<h2>Note</h2>
<ul>
    <li>Ensure that images are placed in the <code>Images/</code> directory relative to the script.</li>
    <li>The images are numbered sequentially (<code>image1.jpeg</code>, <code>image2.jpeg</code>, etc.) and must follow this naming convention for proper functionality.</li>
</ul>
