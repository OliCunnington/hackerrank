

/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    let a, b;
    a = 0
    b = 0
    for (var i = 0; i<nums.length; i++){
        if (nums[i] > a){
            b = a
            a = nums[i]
        }
        else if (nums[i] > b && a != nums[i]){
            b = nums[i]
        }
    }
    return b
}

