# garageParker
check if im backing up and deploy parking aid 

Summary: Use/train imageai to detect my taillights when the backup light is on. When on just needs to send on signal to device to deploy parking aid. Should only work with tail lights in reverse. Should only be my tail lights not others. Should fail off, or on failure parking aid is not deployed.

Parking aid:
It must not obstruct or exist permenantly in the useable garage space. It needs to locate in two planes(x,y).
I thought some on this and to be honest the cheapest/simplest best solution is just some water proof tape on the floor to line up with backup cam lines. But that would not be much fun. Thought about also maybe some sort of laser line emiting light. Probably can be issue since height of ceiling relative to height of car may cut of critical angle of these lights for compact unit, might not though. Also thinking about just a simple motor/stepper with a ball on a string, when on deploys ball. When off retracts ball. 
Parking aid can be seperate from tail light recognition.

Tail light recognition:
Imageai need to download, annotate, train it to recognize my taillights with the reverse lights on. 

Training:
Training to detect my tail lights and my tail lights in reverse, infront of my garage. Because of this just used small training data i could gather my self. 
Took video of my car pulling in and out of the garage forward and reverse. Labeled the images tl for tail light and tlr for taillight reverse. 
ffmpeg video into frames and labeled the frames. 
I think since i just need it to know tail light reverse for my garage and use case it will be fine.
Trained over night and it appears to be working.

