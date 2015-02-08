from collections import defaultdict

def autodict():
    return defaultdict(autodict)

flag_fields = autodict()
symbolic_fields = autodict()

def define_flag_field(event_name, field_name, delim):
    flag_fields[event_name][field_name]['delim'] = delim

def define_flag_value(event_name, field_name, value, field_str):
    flag_fields[event_name][field_name]['values'][value] = field_str

def define_symbolic_field(event_name, field_name):
    # nothing to do, really
    pass

def define_symbolic_value(event_name, field_name, value, field_str):
    symbolic_fields[event_name][field_name]['values'][value] = field_str

def flag_str(event_name, field_name, value):
    string = ""

    if flag_fields[event_name][field_name]:
	print_delim = 0
        keys = flag_fields[event_name][field_name]['values'].keys()
        keys.sort()
        for idx in keys:
            if not value and not idx:
                string += flag_fields[event_name][field_name]['values'][idx]
                break
            if idx and (value & idx) == idx:
                if print_delim and flag_fields[event_name][field_name]['delim']:
                    string += " " + flag_fields[event_name][field_name]['delim'] + " "
                string += flag_fields[event_name][field_name]['values'][idx]
                print_delim = 1
                value &= ~idx

    return string

def symbol_str(event_name, field_name, value):
    string = ""

    if symbolic_fields[event_name][field_name]:
        keys = symbolic_fields[event_name][field_name]['values'].keys()
        keys.sort()
        for idx in keys:
            if not value and not idx:
		string = symbolic_fields[event_name][field_name]['values'][idx]
                break
	    if (value == idx):
		string = symbolic_fields[event_name][field_name]['values'][idx]
                break

    return string

trace_flags = { 0x00: "NONE", \
                    0x01: "IRQS_OFF", \
                    0x02: "IRQS_NOSUPPORT", \
                    0x04: "NEED_RESCHED", \
                    0x08: "HARDIRQ", \
                    0x10: "SOFTIRQ" }

def trace_flag_str(value):
    string = ""
    print_delim = 0

    keys = trace_flags.keys()

    for idx in keys:
	if not value and not idx:
	    string += "NONE"
	    break

	if idx and (value & idx) == idx:
	    if print_delim:
		string += " | ";
	    string += trace_flags[idx]
	    print_delim = 1
	    value &= ~idx

    return string