#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int ice_brick_volume(int radius, int bottle_length, int rim_length) {
  int height = bottle_length - rim_length;
  float area;
  area = (2 * pow(radius, 2)); 
  return area*height;
}