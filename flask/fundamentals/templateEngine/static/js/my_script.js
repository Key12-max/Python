function simpleArraySum(ar) {

    let sum = 0;
    for( let i=0;  i<ar.length;  i++ ){
        sum+=ar[i];
    }
    return sum;
}
print(simpleArraySum([1,2,5,6]))