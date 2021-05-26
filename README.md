# cnvSDF.py

***cnvSDF.py*** converts output of jitech's "SDF Editor" https://joetech.itch.io/sdf-editor  
to Shadertoy, GLSL code.  

It handle **Primitives**  
   
   Box, Frame, Cylynder, InfCylynder, Capsule, Cone, Capped Cone, Round Cone, InfCone  
   Sphere, Ellipsoid, Solid Angle, TriPrism, Hexprism, Torus, CappedTorus, Link,   
   Octahedron, Pyramid, Plane, 
   
  
and **Modifieres**   
 
   Translation, Rotation, Mirror, RepInf, Replim, Elongation
   
  
and **Operators**  
  
  Union, Subtraction, Interection, Onion, Thicken, SmoothUnion, SmoothSubtraction, SumoothIntersection  
    
***How it works?***
  
   ***1.*** Model SDF objects with "SDF Editor".  
   
   ***2.*** Save data as "test.json" which is defalut file name.  
     
   ***3.*** Find "sdf" in Visual Studio Code, and go to line of sdf(vec3 p0) {...}
   
   ***4.*** Copy sdf function from output pane of "SDF Editor" and replace lines of viewSDF.flag.  
   
   ***5.*** Run cnvSDF.py, and copy output lines to head of  viewSDF.flag. 
   
   ***6.*** Close all files of Visual Studio Code.
   
   ***7.*** Open viewSDF.flag with Visual Studio Code with Shadertoy pulugin.
   
   ***8.*** Mouse right button-> Shadertoy:Show GLSL Preview
   
   That's it!
   
   If you want upload it to web,  
     
   ***9.*** Mouse right button-> Shadertoy:Create Protbale GLSL Preview  
     
   You got viewSDF.html.
   
   Just upload it!
   
   
   
   
  
  



