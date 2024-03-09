function createMultiplicationTable(value, maxMultiple = 10) {
 
    const table = [];
  
    const headers = [];
    for (let i = 1; i <= maxMultiple; i++) {
      headers.push(`${value} * ${i}`);
    }
    table.push(headers);
    for (let i = 1; i <= maxMultiple; i++) {
      const row = [];
      for (let j = 1; j <= maxMultiple; j++) {
        row.push(`${i} * ${j} = ${i * j}`);
      }
      table.push(row); 
    }
  
    return table;
  }
  
  const value = 7;
  const maxMultiple = 12;
  const multiplicationTable = createMultiplicationTable(value, maxMultiple);
  for (const row of multiplicationTable) {
    console.log(row.join('\t')); 
  }
  