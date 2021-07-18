# Creating and Modifying 'Mask Layouts' for Sensor Designs

Use the 'mask layouts' of our sensor designs in image format at least as a starting point.

 1. Decide on the largest and/or most common/prevalent *resolution* $\lambda_{\,\textsf{macro}\,}$ expected for the mask layout. For example, 1 mm for most design features. \
    ​
    
 2. Estimate the bounding size of the mask layout. For example, layout height $H_{\,\textsf{layout}}$ = sensor width = 25 mm, layout width $W_{\,\textsf{layout}}$ = sensor length = 45 mm. \
    ​
    
 3. Using image editing software, create an image of height $H_{\,\textsf{layout}}\,/\,\lambda_{\,\textsf{macro}\,}$ pixels and width $W_{\,\textsf{layout}}\,/\,\lambda_{\,\textsf{macro}\,}$ pixels. Set its *image resolution* to $1\,/\,\lambda_{\,\textsf{macro}\,}$ pixels, for reference. Keep in mind the software units. For example:
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Creating-and-Modifying-Mask-Layouts-for-Sensor-Designs/Figure%20(1).png" style="zoom:50%;" /> \
    ​
    
 4. Enable the pixel grid and rulers, optionally, if available.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Creating-and-Modifying-Mask-Layouts-for-Sensor-Designs/Figure%20(2).png" style="zoom:50%;" /> \
    ​
    
 5. On a pixel scale, create the largest design features (of resolution $\lambda_{\,\textsf{macro}\,}$, that is) first. For example:
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Creating-and-Modifying-Mask-Layouts-for-Sensor-Designs/Figure%20(3).png" style="zoom:50%;" /> \
    ​
    
 6. Resize the image to be of height $H_{\,\textsf{layout}}\,/\,\lambda_{\,\textsf{micro}\,}$ pixels and width $W_{\,\textsf{layout}}\,/\,\lambda_{\,\textsf{micro}\,}$ pixels, where $\lambda_{\,\textsf{micro}\,}$ is the smallest underlying resolution. Update its *image resolution* to $1\,/\,\lambda_{\,\textsf{micro}\,}$ pixels, for reference, again. Keep in mind the software units. Use the *nearest neighbor* resampling method and maintain the *aspect ratio*. For example:
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Creating-and-Modifying-Mask-Layouts-for-Sensor-Designs/Figure%20(4).png" style="zoom:50%;" /> \
    ​
    
 7. On the new pixel scale, create the smallest design features (of resolution $\lambda_{\,\textsf{micro}\,}$, that is). For example:
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Creating-and-Modifying-Mask-Layouts-for-Sensor-Designs/Figure%20(5).png" style="zoom:50%;" /> \
    ​

Tip: Use named image layers (as analogous to *SolidWorks* features). For example:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Creating-and-Modifying-Mask-Layouts-for-Sensor-Designs/Figure%20(6).png" style="zoom:50%;" /> \
​
