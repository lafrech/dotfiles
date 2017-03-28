files=(
    .bash_aliases
)

# http://stackoverflow.com/a/246128/4653485
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

make_link()
{

    if [ -L ~/$1 ]
    then
        echo "Remove symlink ~/$1"
        rm ~/$1
    elif [ -f ~/$1 ]
    then
        echo "Backup file ~/$1 into ~/$1.bak"
        mv ~/$1 ~/$1.bak
    fi
    
    echo "Create symlink $script_dir/$1 -> ~/$1"
    ln -sv $script_dir/$1 ~/$1 > /dev/null
}

for file in ${files[@]}
do
    make_link $file
done
