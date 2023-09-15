# Wira : Post Processing Generated masks with GAN Model
## Version 1.0
### What does this code do ? 
* rounds all values to 0 and 1 (from 0 to 1)
* fills holes in the mask 
* finds biggest blob and removes other small blobs 

## Project Info : 
**VERSION** : 1.0

**STAGE** : POST-PROCESS 

**PHASE** : Pelvic Segmentation

**INFO** : Convert model generated body mask to applicable mask 

**BUG** : on leg slices , only one leg is masked 

INPUT CONDITIONS :  
1) input array order must be at [number of slices , rows , columns]

2) input array values must be between 0 and 1 

3) input of the training set must be based on model 4 pre process data


## Todo 
 [ ] when two feets are sepreated , only one of them is returned. there must be a checker for the biggest blob ratio to the second blob
