func interpret(command string) string {
    command = strings.Replace(command, "()", "o", -1)
    return strings.Replace(command, "(al)", "al", -1)
}
