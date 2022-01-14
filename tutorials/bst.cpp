#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int data) {
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

void addNode(int data, Node* head) {
    if (head == NULL) {
        head = new Node(data);
        return;
    }

    if (head->data >= data) {
        if (head->left == NULL) {
            head->left = new Node(data);
            return;
        }

        addNode(data, head->left);
    }

    else {
        if (head->right == NULL) {
            head->right = new Node(data);
            return;
        }

        addNode(data, head->right); 
    }

    return;
}

void deleteNode(int data, Node* head) {
    if (head->data == data) {
        // 
    }
}

void inorder(Node* node) {
    if (node == NULL) return;
    
    inorder(node->left);
    cout << node->data << " ";
    inorder(node->right);

}

int main() {
    Node* head = NULL;
    
    int nodes; 
    cout << "Number of nodes : ";
    cin >> nodes;

    for (int i=0; i<nodes; i++) {
        int x;
        cin >> x;

        if (head == NULL) {
            head = new Node(x);
            continue;
        }

        addNode(x, head);
    }

    if (head == NULL) cout << "NULL" << endl;

    inorder(head);
}