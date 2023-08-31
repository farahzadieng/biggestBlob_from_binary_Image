# Wira : Post Processing Generated masks with GAN Model
## Version 1.0
### What does this code do ? 
* rounds all values to 0 and 1 (from -1 to 1)
* fills holes in the mask 
* finds biggest blob and removes other small blobs 

## Todo 
 [ ] when two feets are sepreated , only one of them is returned. there must be a checker for the biggest blob ratio to the second blob
