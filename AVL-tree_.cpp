/*
//	When I wrote this code, only God and me understood what I was doing.
//	Now, only God knows~~~.

    .--,       .--,
   ( (  \.---./  ) )
    '.__/o   o\__.'
       {=  ^  =}
        >  -  <
       /       \
      //       \\
     //|   .   |\\
     "'\       /'"_.-~^`'-.
        \  _  /--'         `
      ___)( )(___
     (((__) (__)))
*/


#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <windows.h>  // for Sleep

using namespace std;

// Node structure for AVL tree
struct Node {
    int key;
    int height;
    string name;
    string class1;
    string class2;
    Node *left;
    Node *right;

    Node(int k, const string& n, const string& c1, const string& c2)
        : key(k), height(1), name(n), class1(c1), class2(c2), left(nullptr), right(nullptr) {}
};

// AVL tree utility functions
int getHeight(Node* node) {
    return node ? node->height : 0;
}

int getBalance(Node* node) {
    return node ? getHeight(node->left) - getHeight(node->right) : 0;
}

void updateHeight(Node* node) {
    if (node) {
        node->height = max(getHeight(node->left), getHeight(node->right)) + 1;
    }
}

Node* rotateLeft(Node* node) {
    Node* rightChild = node->right;
    node->right = rightChild->left;
    rightChild->left = node;
    updateHeight(node);
    updateHeight(rightChild);
    return rightChild;
}

Node* rotateRight(Node* node) {
    Node* leftChild = node->left;
    node->left = leftChild->right;
    leftChild->right = node;
    updateHeight(node);
    updateHeight(leftChild);
    return leftChild;
}

void insert(Node*& node, int key, const string& name, const string& class1, const string& class2) {
    if (!node) {
        node = new Node(key, name, class1, class2);
        return;
    }

    if (key < node->key)
        insert(node->left, key, name, class1, class2);
    else
        insert(node->right, key, name, class1, class2);

    updateHeight(node);

    int balance = getBalance(node);

    // AVL rotations
    if (balance > 1 && key < node->left->key)
        node = rotateRight(node);
    else if (balance < -1 && key > node->right->key)
        node = rotateLeft(node);
    else if (balance > 1 && key > node->left->key) {
        node->left = rotateLeft(node->left);
        node = rotateRight(node);
    } else if (balance < -1 && key < node->right->key) {
        node->right = rotateRight(node->right);
        node = rotateLeft(node);
    }
}

// Traversals
void preorder(Node* node) {
    if (!node) return;
    cout << node->key << " " << node->name << " " << node->class1 << " " << node->class2 << endl;
    preorder(node->left);
    preorder(node->right);
}

void inorder(Node* node) {
    if (!node) return;
    inorder(node->left);
    cout << node->key << " " << node->name << " " << node->class1 << " " << node->class2 << endl;
    inorder(node->right);
}

// Free memory
void freeTree(Node* node) {
    if (!node) return;
    freeTree(node->left);
    freeTree(node->right);
    delete node;
}

// Parse a line of data
bool parseLine(const string& line, int& key, string& name, string& class1, string& class2) {
    stringstream ss(line);
    if (!(ss >> key >> name >> class1 >> class2)) return false;
    return true;
}

int main() {
    string filename;
    cout << "Please enter the file name in current directory:\n";
    cin >> filename;

    ifstream datafile(filename);
    if (!datafile.is_open()) {
        cerr << "Failed to open file: " << filename << endl;
        return 1;
    }

    cout << "Starting to build the AVL tree from data...\n";
    Node* root = nullptr;
    string line;

    while (getline(datafile, line)) {
        int key;
        string name, class1, class2;
        if (!parseLine(line, key, name, class1, class2)) {
            cerr << "Skipping invalid line: " << line << endl;
            continue;
        }

        insert(root, key, name, class1, class2);
        cout << "Inserted: " << key << " " << name << " " << class1 << " " << class2 << endl;
        // Sleep(1000); // optional pause for debugging
    }

    cout << "\nRoot node: " << root->key << " " << root->name << " " << root->class1 << " " << root->class2 << endl;
    cout << "-----------Inorder Traversal--------------" << endl;
    inorder(root);

    freeTree(root);
    return 0;
}



