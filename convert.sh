a=dungeon-crawl-stone-soup-full
find $a -type f | while read file;
  do mkdir -p $(dirname $file |  sed "s@^$a@big-$a@") &&
  ./$a/hqx/hqx -s 4 $file $(echo $file | sed "s@^$a@big-$a@")
  echo $file
done