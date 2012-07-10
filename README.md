# SubFancy - Sublime Text 2 Fancy interaction plugin

SubFancy adds live editing and metadata support for Fancy to Sublime Text 2.
The communication happens in the background over MessagePack RPC.

Any SubFancy command makes a request to a SubFancy process running in the background (written in Fancy and running a MessagePack RPC server) and deals with its response.

### Planned features so far:

* Jump to class / method definition
* Eval Fancy code in the current context
* Live auto-completion
* Live debugger with support for:
    * breakpoints
    * locals & stack inspection
    * stepping / skipping / jumping callframes