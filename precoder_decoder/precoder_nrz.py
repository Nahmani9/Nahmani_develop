error = 'off'
error = 'on'
mod = 2
input_seq = [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0]


diff_enc_out = [0] * len(input_seq)

for index in range(len(diff_enc_out)):
    if index == 0:
        diff_enc_out[index] = (input_seq[index]) % mod
    else:
        diff_enc_out[index] = (diff_enc_out[index-1] + input_seq[index]) % mod

print("Input:                       ", input_seq)
print("Differential encoder output: ", diff_enc_out)
print("---- channel ----")

recived_sequence = diff_enc_out
if error == 'off':
    print("recived_sequence:            ", recived_sequence)
elif error == 'on':
    error_vec = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    zip_vec = zip(error_vec, recived_sequence)
    recived_sequence = [(x + y) % mod for(x, y) in zip_vec]
    print("recived_sequence:            ", recived_sequence)

decoder_output = [0] * len(input_seq)

for index in range(len(decoder_output)):
    if index == 0:
        decoder_output[index] = (recived_sequence[0]) % mod
    else:
        decoder_output[index] = (recived_sequence[index-1] + recived_sequence[index]) % mod


print("Decoder Output:              ", decoder_output)

error_count = 0
draw = '                              '

for ii in range(len(input_seq)):
    if input_seq[ii] != decoder_output[ii]:
        error_count += 1
        draw += ' ^,'
    else:
        draw += '__,'
print('------------------------------------------------------------------------------------------------')
print("\nInput:                       ", input_seq)
print("Decoder Output:              ", decoder_output)
print(draw)
print("Total bits: %d     error: %d" % (len(input_seq), error_count))
