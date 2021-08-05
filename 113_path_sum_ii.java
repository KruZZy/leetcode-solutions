class Solution {
    private List<List<Integer>> solution; 
    private List<Integer> candidate;
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        solution = new ArrayList<>();
        candidate = new ArrayList<Integer>();

        this.tryExpand(root, targetSum);

        return this.solution;
    }

    public void path(TreeNode root, int remSum) {
        if(root.left == null && root.right == null && remSum == 0) 
            this.solution.add(new ArrayList(this.candidate)); 

        this.tryExpand(root.left, remSum);
        this.tryExpand(root.right, remSum);
    }

    public void tryExpand(TreeNode root, int remSum) {
        if(root != null) {
            this.candidate.add(root.val);
            remSum -= root.val;
            this.path(root, remSum);
            this.candidate.remove(candidate.size()-1);
        }
    }
}