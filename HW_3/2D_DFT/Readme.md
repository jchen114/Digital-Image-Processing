#DFT Discussion

Here I just applied this formula:

F(u,v) = (1/MN) * sum_(x=0,M-1){sum_(y=0,N-1){f(x,y)exp(-j2(pi)(ux/M + vy/N))}}

Notice that I did not add the pi factor in the exponentiation procedure in the frequency_transform function. For some reason, when I add the pi factor in,
the resulting value is always the same. When I leave it off, the values vary as expected. Thus, there will be a factor off from the fft done in numpy.

Time difference = 609.546808725
