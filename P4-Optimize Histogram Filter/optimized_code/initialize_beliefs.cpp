#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector< vector <float> > initialize_beliefs(vector< vector <char> > &grid) {

	// OPTIMIZATION: Which of these variables are necessary?
	// OPTIMIZATION: Reserve space in memory for vectors
  	vector< vector <float> > newGrid;
	vector<float> newRow;

	int height = grid.size();
	int width = grid[0].size();
  
  	newGrid.reserve(height);
  	newRow.reserve(width);

  	// OPTIMIZATION: Is there a way to get the same results 	// without nested for loops?
  	for (int j = 0; j < width; j++) {
      	newRow.push_back(1.0 / ( height * width));
    }
  	for (int i = 0; i < height; i++) {
      	newGrid.push_back(newRow);
    }
	return newGrid;
}