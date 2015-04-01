# Comments on FFT for two images

-	Perform the Fourier transforms for both images.
-	Display the amplitudes of the transforms. This is just the sqrt(real^2 + imag^2). I first shifted the frequencies so that it is centered.
-	The complex coefficients that I get are complex and are of the form Ck = r*exp(jp), where r = |C|, and p is the phase angle. In order to get the phase angle,
	I divided the array by the magnitude of the coefficients. C/|C| = exp(jp). Thus, I can get the phase angle by performing arctan(C/|C|). Next, I normalized the result
	in order to display it.
-	The reconstruction of the image proceeds as normal. I just performed the inverse 2D fourier transform on the fourier transform to collect back the original image. There were
	some complex values that did come up, so I just took the real part of it.
-	The reconstruction of the amplitude is the inverse fourier transform of the magnitude of the transform for each Ck. The magnitude was a very large number. 
	After the inverse fourier transform, I took the real part which is still a very large number. In order to bring this into a suitable scale, I performed a natural log of the result and 
	multiplied it by 20 (from an example provided by numpy). There were some NaN's that I just filtered out. Finally, the result is displayed.
- 	Reconstructing using the phase was pretty straightforward. I just inverse fourier transformed the phase and then took the real part.
-	Here, I multiplied the magnitude of the first image with the phase of the second image. For example if Ck1 = r1*exp(jp1) where Ck1 are the complex coefficients of the first image, r1 is the
	amplitude of the first image and jp1 is the phase of the first image. I replaced jp1 with jp2 of the second image. For each complex coefficient in the first image, I performed Ck1 = r1*exp(jp2).
- 	Same as above, just replaced the first image with the second.