const fs=require('fs');
const s=fs.readFileSync('c:/Users/PCJuan/Desktop/app_concesionario/frontend/src/app/admin/dashboard/page.tsx','utf8');
const regex=new RegExp('<\\/?([A-Za-z0-9_-]+)([^>]*)>','g');
let m;let stack=[];
while((m=regex.exec(s))){
  const full=m[0];
  const name=m[1];
  const isClose=full.startsWith('</');
  const isSelf=full.endsWith('/>')||/\/>\s*$/.test(full)||['path','img','input','link','meta','br'].includes(name.toLowerCase());
  if(!isClose && !isSelf) stack.push({name,idx:m.index});
  else if(isClose){
    const last=stack.pop();
    if(!last){
      console.log('unmatched close',name,'at',m.index);
      console.log('context:\n', s.slice(Math.max(0,m.index-200), m.index+200));
      break;
    }
    if(last.name.toLowerCase()!==name.toLowerCase()){
      console.log('mismatch close',name,'expected',last.name,'at',m.index);
      console.log('stack top:', last.name);
      console.log('context before:\n', s.slice(Math.max(0,m.index-200), m.index));
      console.log('context after:\n', s.slice(m.index, m.index+200));
      break;
    }
  }
}
if(stack.length){console.log('unclosed tags (full):');stack.forEach(sg=>{const linesBefore=s.slice(Math.max(0,sg.idx-30),sg.idx+30);const ln=s.slice(0,sg.idx).split(/\r?\n/).length;console.log(sg.name,'at index',sg.idx,'line',ln);console.log(linesBefore);});}else console.log('all tags closed');
