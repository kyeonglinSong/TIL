#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct TreeNode
{
	string label; // ������ �ڷ�
	TreeNode* parent; // �θ� ��带 ����Ű�� ������
	vector<TreeNode*> children; // �ڼ� ������ ����Ű�� �������� �迭
};

// Ʈ�� ��ȸ
void printLabels(TreeNode* root)
{
	cout << root->label << endl;
	for (int i = 0; i < root->children.size(); i++)
		printLabels(root->children[i]);
}

// Ʈ���� ���� ���ϱ�
int height(TreeNode* root)
{
	int h = 0;
	for (int i = 0; i < root->children.size(); i++)
		h = max(h, 1 + height(root->children[i]));
	return h;
}

// ���� ��ȸ
void preorder(TreeNode* root)
{
	cout << root->label << endl;
	for (int i = 0; i < root->children.size(); i++)
		preorder(root->children[i]);
}

// ���� ��ȸ
void inorder(TreeNode* root)
{
	inorder(root->children[0]);
	cout << root->label << endl;
	inorder(root->children[1]);
}

// ���� ��ȸ
void postorder(TreeNode* root)
{
	for (int i = 0; i < root->children.size(); i++)
		postorder(root->children[i]);
	cout << root->label << endl;
}