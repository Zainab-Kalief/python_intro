# function compare(arr, arr2) {
#   var count = 0
#   if (arr.length == arr2.length) {
#     for (var i = 0; i < arr.length; i++) {
#       for (var j = 0; j < arr2.length; j++) {
#         if (arr[i] == arr2[j]) {
#           count += 1
#           console.log(arr[i], arr2[j]);
#           break;
#         }
#       };
#     };
#   }
#   if (count == arr.length) {
#     console.log(count);
#     return true
#   } else {
#     console.log(count);
#     return false
#   }
# }
#
# console.log(compare([1,2,6,2],[2,1,2,6]));

arr = [1,2,4,6,8,10]
arr2 = [2,1,10,8,6,4]
count = 0
if len(arr) == len(arr2):
    for value in arr:
        for val in arr2:
            if value == val:
                count += 1
                break

if count == len(arr):
    print count
    print True
else:
    print count
    print False
