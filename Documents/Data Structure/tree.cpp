#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct TreeNode
{
	string label; // 저장할 자료
	TreeNode* parent; // 부모 노드를 가리키는 포인터
	vector<TreeNode*> children; // 자손 노드들을 가리키는 포인터의 배열
};

// 트리 순회
void printLabels(TreeNode* root)
{
	cout << root->label << endl;
	for (int i = 0; i < root->children.size(); i++)
		printLabels(root->children[i]);
}

// 트리의 높이 구하기
int height(TreeNode* root)
{
	int h = 0;
	for (int i = 0; i < root->children.size(); i++)
		h = max(h, 1 + height(root->children[i]));
	return h;
}

// 전위 순회
void preorder(TreeNode* root)
{
	cout << root->label << endl;
	for (int i = 0; i < root->children.size(); i++)
		preorder(root->children[i]);
}

// 중위 순회
void inorder(TreeNode* root)
{
	inorder(root->children[0]);
	cout << root->label << endl;
	inorder(root->children[1]);
}

// 후위 순회
void postorder(TreeNode* root)
{
	for (int i = 0; i < root->children.size(); i++)
		postorder(root->children[i]);
	cout << root->label << endl;
}