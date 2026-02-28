# input: yaml.txt, xxxx.pdb(1TNF.pdb)
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/opt/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/opt/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

simulation_time=1
output_directory="./output"

while getopts "t:o:" opt; do
    case $opt in
        t) simulation_time="$OPTARG" ;;
        o) output_directory="$OPTARG" ;;
        *) echo "用法: $0 [-t simulation_time] [-o output_directory] <molecules>"
           echo "  -t  simulation_time: 可选，默认 1"
           echo "  -o  output_directory: 可选，默认 ./output"
           echo "  molecules: 必填，如 8S99.pdb"
           exit 1 ;;
    esac
done
shift $((OPTIND - 1))

if [ -z "$1" ]; then
    echo "用法: $0 [-t simulation_time] [-o output_directory] <molecules>"
    echo "  -t  simulation_time: 可选，默认 1"
    echo "  -o  output_directory: 可选，默认 ./output"
    echo "  molecules: 必填，如 8S99.pdb"
    exit 1
fi
molecules="$1"

cat > yaml.txt << YAMLEOF
task0:
    simulation_type: protein
    molecules: ${molecules}
    simulation_time: ${simulation_time}
    output_directory: ${output_directory}
YAMLEOF


mkdir -p output
conda activate craton
craton simulation yaml -f yaml.txt

root=$(pwd)
all_job=$(find . -name "job.sh" | xargs dirname)
echo all gromacs jobs: $all_job

for job in $all_job; do
    cd $job
    pwd
    bash job.sh
    echo gromacs job done in: $job
    cd $root
done

# output: prod_npt.gro, prod_npt.tpr, prod_npt.xtc