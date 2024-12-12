#pragma once

#include <string>

std::string interpret_string(const std::string &code)
{
    std::string std_out;

    unsigned int tape_pos = 0;
    unsigned int array[30000];

    for (const auto c: code)
    {
        switch (c)
        {
            case '+':
                ++tape_pos;
            break;
            case '-':
                --tape_pos;
            break;
            case '^':
                array[tape_pos]++;
            break;
            case 'v':
                array[tape_pos]--;
            break;
            case '*':
                std_out += std::to_string(array[tape_pos]);
            break;
        }
    }

    return std_out;
}