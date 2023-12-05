with open("2023/inputs/5.txt") as file:
    maps = file.read().split("\n\n")

seeds = list(map(int, maps[0].strip().split(": ")[1].split(" "))) 
maps = [maps[i].strip().split(":\n")[1] for i in range(1, 7+1)]

def return_value(i, key):
    for kv in maps[i].split("\n"):
        kv = kv.strip().split(" ")
        kv = list(map(int, kv))
        if key >= kv[1] and key < kv[1]+kv[2]:
            return kv[0]+key-kv[1]
    return key

loc = []

for j in range(0, int(len(seeds)), 2):
    for seed in range(seeds[j], seeds[j]+seeds[j+1]):
        temp = seed
        for i in range(0, 7):
            temp = return_value(i, temp)
        print(j, temp)
        loc.append(temp) 


print(min(loc))  


# absolutely garbage solution
# had to port it to Rust to have it finish computation in feasible amount of time
# https://files.catbox.moe/uo2f2y.png

'''
use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn return_value(map: &Vec<(i64, i64, i64)>, key: i64) -> i64 {
    for kv in map {
        if key >= kv.1 && key < kv.1 + kv.2 {
            return kv.0 + key - kv.1;
        }
    }
    key
}

fn main() -> io::Result<()> {
    let file = File::open("2023/inputs/5.txt")?;
    let mut reader = BufReader::new(file);
    let mut content = String::new();
    reader.read_to_string(&mut content)?;

    let parts: Vec<&str> = content.split("\n\n").collect();
    let seeds: Vec<i64> = parts[0].split(": ").nth(1).unwrap().split(" ").map(|s| s.parse::<i64>().unwrap()).collect();

    let mut maps = Vec::new();
    for part in &parts[1..] {
        let lines: Vec<&str> = part.lines().collect();
        let map = lines[1..].iter().map(|line| {
            let kv = line.split(" ").map(|s| s.parse::<i64>().unwrap()).collect::<Vec<_>>();
            (kv[0], kv[1], kv[2])
        }).collect::<Vec<_>>();
        maps.push(map);
    }

    let mut loc = Vec::new();

    for j in (0..seeds.len()).step_by(2) {
        let mut hmm = Vec::new();
        for seed in seeds[j]..seeds[j] + seeds[j+1] {
            let mut temp = seed;
            for i in 0..7 {
                temp = return_value(&maps[i], temp);
            }
            hmm.push(temp);
        }
        loc.push(hmm.iter().min().unwrap().clone());
        println!("{}: {:?}", j, loc);
    }

    println!("{}", loc.iter().min().unwrap());

    Ok(())
}
'''
