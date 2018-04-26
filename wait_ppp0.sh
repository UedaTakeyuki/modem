# http://qiita.com/bsdhack/items/29400b9ed989cd67b1db
cwd=`dirname "${0}"`
# ${0} が 相対パスの場合は cd して pwd を取得
expr "${0}" : "/.*" > /dev/null || cwd=`(cd "${cwd}" && pwd)`
echo $cwd

conf=""
command=""

ini_file=$cwd/${0##*/}
ini_file=${ini_file%.*}
ini_file=${ini_file}.ini
if [ $# -eq 1 ]; then
	ini_file=$cwd/$1
fi
echo $ini_file

. $ini_file

count=0
while [ `ifconfig ppp0 | wc -l` = 0 ]
do
  sleep 10
  ((count += 1))
  if [ -v wait_times -a -v after_wait_command -a $count -gt ${wait_times} ]; then
    ${after_wait_command}
  fi
  echo $count
done
exit 0
