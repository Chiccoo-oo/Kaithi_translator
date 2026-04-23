#include <bits/stdc++.h>
using namespace std;

typedef vector<double> vec;

// Function to compute gradient (USER DEFINED)
vec gradient(vec x) {
    int n = x.size();
    vec grad(n);

    // Example: f(x, y) = x^2 + y^2
    // Modify this for your function

    grad[0] = 2 * x[0]; // df/dx
    grad[1] = 2 * x[1]; // df/dy

    return grad;
}

// Function value (optional, for display)
double function_value(vec x) {
    return x[0]*x[0] + x[1]*x[1];
}

int main() {
    int n;
    cout << "Enter number of variables: ";
    cin >> n;

    vec x(n);
    cout << "Enter initial values:\n";
    for (int i = 0; i < n; i++) cin >> x[i];

    double alpha, tol;
    int max_iter;

    cout << "Enter learning rate: ";
    cin >> alpha;

    cout << "Enter tolerance: ";
    cin >> tol;

    cout << "Enter max iterations: ";
    cin >> max_iter;

    for (int iter = 0; iter < max_iter; iter++) {
        vec grad = gradient(x);

        double norm = 0;
        for (double g : grad) norm += g * g;
        norm = sqrt(norm);

        if (norm < tol) {
            cout << "Converged!\n";
            break;
        }

        for (int i = 0; i < n; i++) {
            x[i] = x[i] - alpha * grad[i];
        }
    }

    cout << "\nOptimal Solution:\n";
    for (int i = 0; i < n; i++) {
        cout << "x" << i+1 << " = " << x[i] << endl;
    }

    cout << "Minimum Value = " << function_value(x) << endl;

    return 0;
}