#include <vector>

class ProductOfNumbers {
    /**
     * Design an algorithm that accepts a stream of integers and retrieves the product of 
     * the last k integers of the stream.
     * 
     * Implement the ProductOfNumbers class:
     *      - ProductOfNumbers() Initializes the object with an empty stream.
     *      - void add(int num) Appends the integer num to the stream.
     *      - int getProduct(int k) Returns the product of the last k numbers in the current list. 
     *        You can assume that always the current list has at least k numbers.
     * 
     * The test cases are generated so that, at any time, the product of any contiguous sequence 
     * of numbers will fit into a single 32-bit integer without overflowing.
     */
   private:
    std::vector<int> prefix;
    int size = 0;

   public:
    ProductOfNumbers() {
        prefix.push_back(1);
        size = 0;
    }

    void add(int num) {
        if (num == 0) {
            prefix = {1};
            size = 0;
        } else {
            prefix.push_back(prefix[size] * num);
            size++;
        }
    }

    int getProduct(int k) {
        if (k > size) {
            return 0;
        }

        return prefix[size] / prefix[size - k];
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */