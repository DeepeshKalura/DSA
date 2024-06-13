fn main() {
    let arr:[u32; 6]= [1,2,3,4,5, 8];
    let key:u32 = 6;

    println!("{}", linear_search(&arr, key));
}


pub fn linear_search(arr: &[u32], key: u32) -> bool {
    for &i in arr{
        if key == i { return true; }
    }
    return false;
    
}