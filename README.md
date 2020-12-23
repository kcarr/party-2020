# pygame-primer
This started by following the pygame primer from realpython.com. It quickly devolved to a party gopher (rendered from an animated gif) avoiding the coronavirus using masks and collecting toilet paper.

Happy 2020, y'all!

## The Process

### The Divergence
I was following the primer when it got to the part of adding jets and missiles and clouds. I realized that it's 2020, and I didn't want jets and missiles and clouds, I wanted a gopher (shoutout to my awesome coworker Vera), coronavirus, masks, and toilet paper (another shoutout to another awesome coworker Christina).

### The cleanup
I also realized that the primer had everything in one big ol' file. That didn't seem right from a coding standpoint. So I made modules, and classes, and extended classes, and images, and a pre-processor so that pygame could actually "gifify" the images that made up the original gif. I'm pretty sure that not all of the best practices were followed, but I'm also happy with the increased DRY-ness I added to this project.

### The conclusion
This was a fun project and I know that I'll continue tinkering with it as time goes on! I hope you enjoy it as much as I did.

## How to make it all run
You'll need `python3`. And `pygame`. And probably some of the other packages this depends on. I'll get a better writeup soon, and maybe some automagical package downloading/containerizing (which will likely result in an shoutout to another awesome coworker Tim). Anywho, I'm sure you can use your own developer awesomeness to get all the packages. Then open a terminal, go to the right folder, and run this by typing `python3 main.py`. And then enjoy!