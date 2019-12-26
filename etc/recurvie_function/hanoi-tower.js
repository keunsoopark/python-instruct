function hanoi (num, from, to, other) {
    if (num === 0)  return;
    console.log(`num: ${num}, from: ${from}, to: ${to}, other: ${other}.`)
    hanoi (num - 1, from, other, to);
    hanoi (num - 1, other, to, from);
}

hanoi(4, 0, 1, 2);