function strip_test_item()
{
    if [ "${1: -1}" == "." ]; then
        strip_test_item "${1%?}" # Remove the last character
    else
        echo "$1"
    fi
}

### Main ###
#bash run_test_module.sh test_fundamental.TestBasicPrintSerial.print_serial
if [ -z $1 ]; then
    for test in $(ls *.py); do
      echo -e "Running test module: ${test%.*} ..."
      sudo python -m unittest -f ${test%.*}
    done
else
    test_item=$(strip_test_item "$1")
    echo -e "Running test module: ${test_item}"
    sudo python -m unittest -f -v ${test_item}
    if [ $? -ne 0 ]; then
        echo -e
        echo -e "error return"
        echo -e
    fi
fi
